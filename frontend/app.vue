<template>
  <div :dir="currentLanguage==='en'? 'ltr':'rtl'" class="bg-[#FDF8F8]">
    <Header class="w-full fixed top-0 z-40 " :product-list="categories"/>
    <div class="w-full bg-white h-[11.6vw] "></div>
    <NuxtPage />
<TheFooter/>
<LanguageSelector v-if="isLangSelected===false"/>
<TheLoading v-if="isLoaded===true" :class="['transition-all duration-300 ease-out', isLoaded?'opacity-100':'opacity-0' ]" />
  </div>
</template>
<script>
import Header from './components/global/TheHeader.vue'
import TheFooter from './components/global/TheFooter.vue';
import LanguageSelector from './components/global/LanguageSelector.vue';
import TheLoading from './components/global/TheLoading.vue';
import {loadingStore} from '~/store/loading-state.js'
import { footerStore } from './store/footer-state';
export default{
  components:{
    Header,TheFooter,TheLoading,LanguageSelector
  },
  methods:{
   async fetchCategories(){
    fetch('https://admin.jahanexport.com/products/categories/') 
      .then(response => response.json())
      .then(data => {
        this.categories = data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
         this.$router.push('/notFound');
      });
   },
   async fetchFooterData(){
      try {
        const response = await fetch('https://admin.jahanexport.com/api/footer/');
        if (!response.ok) {
          this.$router.push('/notFound');
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        this.footerState.setAddress(result.address);
        this.footerState.setArabicAddress(result.address_arabic)
        this.footerState.setPersianAddress(result.address_persian)
        this.footerState.setInstagram(result.instagram);
        this.footerState.setWhatsapp(result.Whatsapp);
        this.footerState.setEmail(result.email);
        this.footerState.setPhoneNumber(result.phone_number)
        this.footerState.setFooterCaption(result.footer_caption)
        this.footerState.setFooterArabicCaption(result.footer_caption_arabic)
        this.footerState.setFooterPersianCaption(result.footer_caption_persian)
        this.footerState.setLinkedin(result.linkedin)
        this.footerState.setLocation(result.location_link)
      } catch (error) {
        console.error("Error fetching data:", error);
         this.$router.push('/notFound');
      }
    }
  },
  data(){
return {
  footerState : footerStore(),
  loadingStore: loadingStore(),
  isLoaded:false,
  isLangSelected:true,
  categories:[],
}
  },
  watch:{
   'loadingStore.isLoading'(newValue) {
      this.isLoaded = newValue
    },
  },
  mounted(){
    this.fetchCategories();
    this.fetchFooterData();
    const lang = localStorage.getItem('langSelected') || ''
    this.isLangSelected = lang!== ''
  }
}
</script>
<style>

</style>
