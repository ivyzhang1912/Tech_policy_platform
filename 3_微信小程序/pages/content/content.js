// pages/content/content.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // link: 'http://172.20.10.10:5000/',
    changestar: 'false',
    star: '/images/收藏.png',
    starselected: '/images/收藏selected.png',
    nbtitle: '政策详情',
    nbfontcolot: 'white',
    nbbgcolor: '#2151d1',
    res: {},
    cur: {},
    position: { value: 'bottom', text: '' },
  },
  star(){
    let flag = this.data.changestar
    if(flag == 'true'){
      this.setData({
        changestar: 'false'
      })
    }else{
      this.setData({
        changestar: 'true'
      })
    }
    let openid = app.globalData.openid;
    let pid = this.data.res.pid;
    wx.request({
      url: app.globalData.link + 'adddeletestar/' + openid + '/' + String(pid) + '/' + this.data.changestar,
      header: {
        'content-type': 'application/json'
      },
      success: function(response) {      
        console.log('star/delete success');
      }
    })
  },
  handlePopup(e) {
    const { item } = e.currentTarget.dataset;

    this.setData(
      {
        cur: item,
      },
      () => {
        this.setData({ visible: true });
      },
    );
  },
  onVisibleChange(e) {
    this.setData({
      visible: e.detail.visible,
    });
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    let openid = app.globalData.openid;
    let pid = options.pid;
    var that = this;
    wx.request({
      url: app.globalData.link + 'getcontent/' + openid + '/' + String(pid),
      header: {
        'content-type': 'application/json'
      },
      success: function(response) {
        console.log(response); 
        that.setData({
          res: response.data,
          'position.text': response.data.abstract,  // 修改字典内的字段时需要将字典和键用引号引起来
          changestar: response.data.flag
        })
      },
      fail: function(response){
        console.log(response);
      }

    })
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