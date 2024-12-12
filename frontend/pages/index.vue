<template>
  <ImageSlider :sliderData="sliderData"/>
  <BussinessOverview :slogan="slogan" :sloganAr="sloganAr" :sloganIr="sloganIr"  class="w-full overflow-x-hidden"/>
  <ProductList :products="productsData" class="w-full overflow-x-hidden"/>
  <SaleFestival v-if="hasFestival" :sale-festival="saleFestival" class="w-full overflow-x-hidden"/>
  <VideoPlayer v-if="videoUrl.length>0" :videoUrl="videoUrl"/>
 
</template>

<script>
import ImageSlider from '@/components/landng/ImageSlider.vue'
import BussinessOverview from '~/components/landng/BussinessOverview.vue';
import ProductList from '~/components/landng/ProductList.vue';
import SaleFestival from '~/components/landng/SaleFestival.vue';
import VideoPlayer from '~/components/landng/VideoPlayer.vue';
import { useI18n } from 'vue-i18n';
import { footerStore } from '~/store/footer-state.js';
import {loadingStore} from '~/store/loading-state.js';

export default {
  name: 'MyComponent',
  setup() {
    const { t, locale } = useI18n();
    onMounted(() => {
            const savedLanguage = localStorage.getItem('appLanguage');
            if (savedLanguage) {
                locale.value = savedLanguage;
            }

        });
    function changeLanguage(lang) {
      locale.value = lang;
    }
    const  products=[
        {
          titleAr:'پسته احمد آقایی',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'پسته کله قوچی',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'پسته احدی',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'پسته اکبری',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'بادام هندی',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'بادام درختی',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'روغن زیتون',
          title:'Mr Ahmad pistachio'
        },
        {
          titleAr:'برنج اعلای شمال',
          title:'Mr Ahmad pistachio'
        },
      ];
    const currentLanguage = computed(() => locale.value);
    return { t, changeLanguage,  currentLanguage, products   };
  },
  mounted(){
      this.fetchData()
      useHead({
      title: this.t('jahanExport') + " | " + this.t('home')
    });
    console.log(this.videoUrl)
  },
  data(){
return {
  store: footerStore(),
  loadingState: loadingStore(),
  lang:'en',
  instagram:'',
  email:'',
  phoneNumber:'',
  linkedIn:'',
  whatsApp:'',
  locationLink:'',
  footerCaption:'',
  footerCaptionArabic:'',
  footerCaptionPersian:'',
  address:'',
  addressArabic:'',
  addressPersian:'',
  sloganAr:'',
  sloganIr:'',
  slogan:'',
  videoUrl:'',
  sliderData:[],
  productsData:[],
  saleFestival:{
    imageUrl:'',
    discount:'',
    title:'',
    titleAr:'',
    titleIr:'',
    caption:'',
    captionAr:'',
    captionIr:'',
    hasFestival : false,
  }
}
  },
  components:{
    ImageSlider,
    BussinessOverview,
    ProductList,
    SaleFestival,
    VideoPlayer
  },
  methods:{
   async fetchData(){
      this.loadingState.setLoading(true);
  try {
    const response = await fetch('https://admin.jahanexport.com/');
    const text = await response.text();
    const data = JSON.parse(text);
    this.instagram = data.instagram;
    this.email = data.email;
    this.phoneNumber = data.phone_number;
    this.linkedIn = data.linkedin;
    this.whatsApp = data.whatsapp;
    this.locationLink = data.location_link;
    this.videoUrl = data.home_controllers[0].video_url;
    this.slogan = data.slogan;
    this.sloganAr = data.slogan_arabic;
    this.sloganIr = data.slogan_persian;
    this.addressArabic = data.address_arabic;
    this.addressPersian = data.address_persian;
    this.address = data.address;
    this.footerCaptionArabic = data.footer_caption_arabic;
    this.footerCaptionPersian = data.footer_caption_persian;
    this.footerCaption = data.footer_caption;
    this.sliderData = data.home_controllers[0].slider_data;
    this.productsData = data.home_controllers[0].products;
    const festival = data.home_controllers[0].sale_festivals;
    if(festival!==null){
      this.saleFestival.caption = festival.caption;
    this.saleFestival.captionAr = festival.caption_arabic;
    this.saleFestival.captionIr = festival.caption_persian;
    this.saleFestival.title = festival.title;
    this.saleFestival.titleAr = festival.title_arabic;
    this.saleFestival.titleIr = festival.title_persian;
    this.saleFestival.discount = festival.discount;
    this.saleFestival.imageUrl = festival.image;
    this.hasFestival = true
    }else{
      this.hasFestival = false;
    }
    this.loadingState.disableLoading();
  } catch (error) {
    this.loadingState.disableLoading();
    console.error('Error fetching or parsing data:', error);
    this.$router.push('/notFound');
  } finally {
    // Always set loading to false once the data is fetched or an error occurs
  }
    }
  }
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');


.cairo {
  font-family: "Cairo", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
  font-variation-settings: "slnt" 0;
}
.montserrat{
  font-family: "Montserrat", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}
</style>