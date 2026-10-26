// app.js
App({
  globalData: {
    userInfo: null,
    openid: '',
    link: 'http://172.20.10.10:5000/',
  },
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    var that = this;
    wx.login({   
      success: function(res) {    //请求自己后台获取用户openid
        wx.request({     
          url: that.globalData.link + 'login/' + res.code,
          success: function(response) {     
            var openid = response.data.openid;   
            // console.log(response);
            console.log('请求获取openid: ' + openid);     
            that.globalData.openid = openid;
          }
        }) 
      }
    })
  },
  // 下拉
  onPageScroll: function(e) {
    if (e.scrollTop < 0) {
      wx.pageScrollTo({
        scrollTop: 0
      })
    }
  },
})
