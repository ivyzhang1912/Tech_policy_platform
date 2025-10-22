// pages/push/push.js
const app = getApp()


const match = (v1, v2, size) => v1.toString().slice(0, size) === v2.toString().slice(0, size);

Page({

  /**
   * 页面的初始数据
   */
  options: {
    styleIsolation: 'apply-shared',
  },
  data: {
    // link: 'http://172.20.10.10:5000/',
    push_policy: [],
    value: 0,
  },

  // 选项卡
  onTabsChange(event) {
    console.log(`Change tab, tab-panel value is ${event.detail.value}.`);
  },

  onTabsClick(event) {
    console.log(`Click tab, tab-panel value is ${event.detail.value}.`);
    this.setData({
      value: event.detail.value
    })
    var that = this;
    let openid = app.globalData.openid;
    let value = this.data.value;
    wx.request({
      url: app.globalData.link + 'push/' + openid + '/' + value,
      success: (res) => {
        console.log(res.data);
        that.setData({
          push_policy: res.data
        })
      }
    })
  },

  onStickyScroll(event) {
    console.log(event.detail);
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
    var that = this;
    let openid = app.globalData.openid;
    let value = this.data.value;
    wx.request({
      url: app.globalData.link + 'push/' + openid + '/' + value,
      success: (res) => {
        that.setData({
          push_policy: res.data
        })
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