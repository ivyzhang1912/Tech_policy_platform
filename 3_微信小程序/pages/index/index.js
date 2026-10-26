// index.js
import Message from 'tdesign-miniprogram/message/index';
// 获取应用实例
const app = getApp()

Page({
  data: {
    openid: '',
    userInfo: {},
    hasUserInfo: false,
    canIUseGetUserProfile: false,
    img1: '/images/type/lljl.png',
    img2: '/images/type/wdsc.png',
    img3: '/images/type/xxtz.png',
    confirmBtn: { content: '确定', variant: 'base' },
    dialogKey: '',
    showText: false,
    showMultiText: false,
    showTextAndTitle: false,
    showMultiTextAndTitle: false,
    otherinfo: [{
      'infotit': '联系我们',
      'info':'开发团队：pyer3.0\n所属单位：南农大自然语言处理学社\n客服微信：wxid_syowupj81wx712',
      'src': '/images/联系我们.png'
    }, {
      'infotit': '关于我们',
      'info':'开发团队：pyer3.0\n所属单位：南农大自然语言处理学社\n客服微信：wxid_syowupj81wx712',
      'src': '/images/关于我们.png'
    }]
  },
  to2nd(event) {
    var currentmine = event.currentTarget.dataset.mine;
    console.log('点击我的部分为' + currentmine);
    wx.navigateTo({ 	
      url: '/pages/mine/mine?mine=' + currentmine
    })
  },
  showDialog(e) {
    const { key } = e.currentTarget.dataset;
    this.setData({ [key]: true, dialogKey: key });
  },

  closeDialog() {
    const { dialogKey } = this.data;
    this.setData({ [dialogKey]: false });
  },
  showCloseMessage() {
    Message.info({
      context: this,
      offset: ['20rpx', 32],
      content: '目前暂无相关消息',
      duration: -1,
      // action: '按钮',
      closeBtn: true,
    });
  },
  // 获取用户信息
  onLoad() {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
    }
  },
  getUserProfile(e) {
    // 推荐使用 wx.getUserProfile 获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
    // 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
        console.log(res.userInfo);
      }
    });
  },
  getUserInfo(e) {
    // 不推荐使用 getUserInfo 获取用户信息，预计自2021年4月13日起，getUserInfo将不再弹出弹窗，并直接返回匿名的用户个人信息
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },

})