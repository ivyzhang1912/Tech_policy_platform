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
    choice_policy_ipt: [],
    choices: {
      value: '政策通知',
      options: [
        {
          value: '政策通知',
          label: '政策通知',
        },
        {
          value: '政策解读',
          label: '政策解读',
        },
        {
          value: '最新资讯',
          label: '最新资讯',
        },
      ],
    },
    timer: {
      value: '全部时间',
      options: [
        {
          value: '全部时间',
          label: '全部时间',
        },
        {
          value: '2023年',
          label: '2023年',
        },
        {
          value: '2022年',
          label: '2022年',
        },
        {
          value: '2021年',
          label: '2021年',
        },
      ],
    },
    area: '',
    inputValue: ''
  },
  search_input:function(event){	
		this.setData({  
			inputValue: event.detail.value 
		})
	},
  MsgUp:function(event){
		// event指点击时间本身，通过输入事件同步数据
    let inpvalue = this.data.inputValue;
    var that = this;
		if(inpvalue){
			wx.showToast({
        title: '搜索中...',
				duration:100000000,
				mask: true,
				icon: 'loading'
        });
      let cp = that.data.choice_policy;
      // console.log(cp);
      for (let i = 0; i < cp.length; i++) {
        if(cp[i].title.includes(inpvalue)){
          that.data.choice_policy_ipt.push(cp[i])
        }
      }
      if(that.data.choice_policy_ipt.length == 0){
        wx.hideToast();
        wx.showModal({
        	title: '提示',
        	content: '未找到该政策',
        })
      }else{
        wx.hideToast();
        let cpi = that.data.choice_policy_ipt;
        that.setData({
          choice_policy: cpi,
          choice_policy_ipt: []
        })
      }
	}
	},
  onChange(e) {
    let v = e.detail.value;
    // console.log(v);
    if(v == '政策通知' || v == '政策解读' || v == '最新资讯'){
      this.setData({
        'choices.value': v,
      });
    }
    else{
      this.setData({
        'timer.value': v,
      });
    }
    let type = this.data.choices.value;
    let t = this.data.timer.value;
    let cnt_type = this.data.nbtitle;
    var that = this;
    let area = this.data.area;
    wx.request({
      url: app.globalData.link + 'gettype/' +  cnt_type + '/' + type + '/' + t + '/' + area,
      success: function(res){
        that.setData({
          choice_policy: res.data
        })
      }
    })
  },
  tocontent(event) {
    var currentid = event.currentTarget.dataset.id;
    console.log('点击政策id为' + String(currentid));
    wx.navigateTo({ 	
      url: '/pages/content/content?pid=' + String(currentid)
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    let cnt_type = options.type;
    let area = options.area;
    this.setData({
      nbtitle: cnt_type,
      area: options.area
    })
    let type = this.data.choices.value;
    let t = this.data.timer.value;
    var that = this;
    wx.request({
      url: app.globalData.link + 'gettype/' +  cnt_type + '/' + type + '/' + t + '/' + area,
      success: function(res){
        that.setData({
          choice_policy: res.data
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