// pages/knowledge_lib_2nd/knowledge_lib_2nd.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // link: 'http://172.20.10.10:5000/',
    nbtitle: '',
    nbfontcolot: 'white',
    nbbgcolor: '#2151d1',
    choice_policy: [],
  },
  onChange(e) {
    this.setData({
      'choices.value': e.detail.value,
    });
  },
  tocontent(event) {
    var currentid = event.currentTarget.dataset.pid;
    console.log('点击政策id为' + String(currentid));
    wx.navigateTo({ 	
      url: '/pages/content/content?pid=' + String(currentid)
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.setData({
      nbtitle: options.mine,
    })
    var that = this;
    let type = options.mine;
    if(type == '浏览记录' || type == '我的收藏'){
      wx.request({
        url: app.globalData.link + 'getmine/' + app.globalData.openid + '/' + type,
        success: function(response) {      
          that.setData({
            choice_policy: response.data
          })
        }
      })
    }
    else{
      let area = options.area;
      wx.request({
        url: app.globalData.link + 'search/' + type + '/' + area, 
        success: function(response) {      
          that.setData({
            choice_policy: response.data
          })
        }
      })
    }
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})