// pages/knowledge_lib/knowledge_lib.js
const app = getApp()
const areaList = {
  provinces: {
    100000: '国家级',
    110000: '省市',
  },
  cities: {
    100001: '',
    110100: '安徽',
    110200: '北京',
    110300: '重庆',
    110400: '福建',
    110500: '广东',
    110600: '广西',
    110700: '贵州',
    110800: '甘肃',
    110900: '河北',
    111000: '黑龙江',
    111100: '河南',
    111200: '湖北',
    111300: '湖南',
    111400: '海南',
    111500: '吉林',
    111600: '江苏',
    111700: '江西',
    111800: '辽宁',
    111900: '内蒙古',
    112000: '宁夏',
    112100: '青海',
    112200: '山西',
    112300: '上海',
    112400: '山东',
    112500: '四川',
    112600: '陕西',
    112700: '天津',
    112800: '西藏',
    112900: '新疆',
    113000: '云南',
    113100: '浙江',
  },
  counties: {
    100001: '',
    110100: '',
    110101: '合肥',
    110102: '宿州',
    110105: '安庆',
    110106: '蚌埠',
    110107: '豪州',
    110108: '池州',
    110109: '滁州',
    110201: '北京市',
    110301: '重庆市',
    110400: '',
    110401: '福州',
    110402: '龙岩',
    110403: '南平',
    110403: '宁德',
    110404: '莆田',
    110405: '泉州',
    110406: '三明',
    110407: '漳州',
    110500: '',
    110501: '广州',
    110502: '佛山',
    110503: '潮州',
    110504: '东莞',
    110600: '',
    110601: '北海',
    110602: '百色',
    110603: '崇左',
    110604: '防城港',
    110700: '',
    110701: '安顺',
    110702: '毕节',
    110703: '贵阳',
    110704: '贵安',
    110800: '',
    110801: '白银',
    110802: '定西',
    110803: '甘南',
    110804: '嘉峪关',
    110900: '',
    110901: '石家庄',
    110902: '保定',
    110903: '沧州',
    110904: '承德',
    111000: '',
    111001: '齐齐哈尔',
    111002: '大庆',
    111003: '大兴安岭',
    111004: '哈尔滨',
    111100: '',
    111101: '漯河',
    111102: '安阳',
    111103: '鹤壁',
    111104: '焦作',
    111200: '',
    111201: '恩施',
    111202: '鄂州',
    111203: '黄冈',
    111204: '黄石',
    111300: '',
    111301: '长沙',
    111302: '常德',
    111303: '衡阳',
    111304: '怀化',
    111400: '',
    111401: '澄迈',
    111402: '乐东',
    111403: '屯昌',
    111404: '万宁',
    111500: '',
    111501: '长春',
    111502: '白城',
    111503: '白山',
    111504: '吉林',
    111600: '',
    111601: '宿迁',
    111602: '无锡',
    111603: '常州',
    111604: '淮安',
    111605: '连云港',
    111606: '南京',
    111607: '南通',
    111608: '苏州',
    111609: '泰州',
    111610: '徐州',
    111611: '盐城',
    111612: '扬州',
    111613: '镇江',
    111700: '',
    111701: '抚州',
    111702: '赣州',
    111703: '吉安',
    111704: '景德镇',
    111800: '',
    111801: '朝阳',
    111802: '沈阳',
    111803: '鞍山',
    111804: '本溪',
    111900: '',
    111901: '阿拉善',
    111902: '包头',
    111903: '巴彦淖尔',
    111904: '赤峰',
    112000: '',
    112001: '石嘴山',
    112002: '固原',
    112003: '吴忠',
    112004: '银川',
    112100: '',
    112101: '海北',
    112102: '海东',
    112103: '海南藏族',
    112104: '海西',
    112200: '',
    112201: '长治',
    112202: '大同',
    112203: '晋城',
    112204: '晋中',
    112300: '',
    112301: '上海市',
    112400: '',
    112401: '滨州',
    112402: '德州',
    112403: '东营',
    112404: '菏泽',
    112500: '',
    112501: '阿坝',
    112502: '广安',
    112503: '广元',
    112504: '乐山',
    112600: '',
    112601: '安康',
    112602: '宝鸡',
    112603: '汉中',
    112604: '商洛',
    112700: '',
    112701: '天津市',
    112800: '',
    112801: '阿里',
    112802: '昌都',
    112803: '拉萨',
    112804: '林芝',
    112900: '',
    112901: '阿克苏',
    112902: '阿拉尔',
    112903: '阿勒泰',
    112904: '石河子',
    113000: '',
    113001: '红河',
    113002: '保山',
    113003: '楚雄',
    113004: '大理',
    113100: '',
    1131001: '杭州',
    1131002: '湖州',
    1131003: '嘉兴',
    1131004: '金华',
  },
};

const getOptions = (obj, filter) => {
  const res = Object.keys(obj).map((key) => ({ value: key, label: obj[key] }));

  if (filter) {
    return res.filter(filter);
  }

  return res;
};

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
    img1: '/images/type/rczc.png',
    img2: '/images/type/cxcy.png',
    img3: '/images/type/sszc.png',
    img4: '/images/type/qyjy.png',
    img5: '/images/type/cyfz.png',
    img6: '/images/type/zdxm.png',
    img7: '/images/type/jlbt.png',
    img8: '/images/type/zfcg.png',
    hot_policy: [],
    provinces: getOptions(areaList.provinces),
    cities: [],
    counties: [],
    area: '全部地区',
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
    let area = this.data.area;
		if(inpvalue){
			wx.showToast({
        title: '搜索中...',
				duration:100000000,
				mask: true,
				icon: 'loading'
        });
			wx.request({
				url: app.globalData.link + 'search/' + inpvalue + '/' + area, 
				success: function(res) {
					// console.log(res.data);
					if(res.data.length==0){
						wx.hideToast();
						wx.showModal({
							title: '提示',
							content: '未找到该政策',
						})
					}
					else{
						wx.hideToast();
						wx.navigateTo({
							url: "/pages/mine/mine?mine=" + inpvalue + '&area=' + area
						})
					}
				},	
		});		
	}
	},
  lifetimes: {
    ready() {
      const { provinces } = this.data;
      const { cities, counties } = this.getCities(provinces[0].value);

      this.setData({ cities, counties });
    },
  },
  onColumnChange(e) {
    console.log('pick:', e.detail);
    const { column, index } = e.detail;
    const { provinces, cities } = this.data;

    if (column === 0) {
      // 更改省份
      const { cities, counties } = this.getCities(provinces[index].value);

      this.setData({ cities, counties });
    }

    if (column === 1) {
      // 更改城市
      const counties = this.getCounties(cities[index].value);

      this.setData({ counties });
    }

    if (column === 2) {
      // 更改区县
    }
  },

  getCities(provinceValue) {
    const cities = getOptions(areaList.cities, (city) => match(city.value, provinceValue, 2));
    const counties = this.getCounties(cities[0].value);

    return { cities, counties };
  },

  getCounties(cityValue) {
    return getOptions(areaList.counties, (county) => match(county.value, cityValue, 4));
  },

  onPickerChange(e) {
    const { value, label } = e.detail;

    console.log('picker confirm:', e.detail);
    this.setData({
      areaVisible: false,
      areaValue: value,
      areaText: label.join(' '),
      area: label.join(',')
    });
  },

  onPickerCancel(e) {
    console.log('picker cancel', e.detail);
    this.setData({
      areaVisible: false,
    });
  },

  onAreaPicker() {
    this.setData({ areaVisible: true });
  },

  tocontent(event) {
    var currentid = event.currentTarget.dataset.pid;
    console.log('点击政策id为' + String(currentid));
    wx.navigateTo({ 	
      url: '/pages/content/content?pid=' + String(currentid)
    })
  },
  to2nd(event){
    var currenttype = event.currentTarget.dataset.type;
    var area = this.data.area;
    console.log('地区为' + area);
    console.log('点击政策内容类型为' + currenttype);
    wx.navigateTo({ 	
      url: '/pages/knowledge_lib_2nd/knowledge_lib_2nd?type=' + currenttype + '&area=' + area,
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
   var that = this;
   wx.request({
     url: app.globalData.link + 'gethotpolicy',
     success: function(res){
      //  console.log(res);
      that.setData({
          hot_policy: res.data 
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