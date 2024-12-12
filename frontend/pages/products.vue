<template>
    <div>
        <div class="h-[11.1vw] md:h-[5.5vw] w-full"></div>
    <div class="w-full px-[3.75vw] md:px-[10.8vw]">
        <div :class="['flex space-x-[0.5vw] select-none items-center w-full', currentLanguage!=='en' ? 'justify-start' : 'justify-start flex-row-reverse']">
    <div :class="[ currentLanguage ==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat'),'text-[5.5vw] text-[#791A4D] md:text-[1.6vw]']">{{ currentLanguage==='ar' ? firstCategoryArabic : (currentLanguage==='ir' ? firstCategoryPersian : firstCategory) }}</div>
   <div>
    <svg :class="[currentLanguage!=='en' ? 'rotate-180':'rotate-0','w-[5.5vw] md:w-[1.6vw] md:h-[1.6vw] h-[5.5vw] ']" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g id="navigate_next">
<path id="icon" d="M12.6 12L8 7.4L9.4 6L15.4 12L9.4 18L8 16.6L12.6 12Z" fill="#791A4D"/>
</g>
</svg>

   </div>
<div :class="[ currentLanguage ==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat'),'text-[5.5vw] text-[#791A4D] md:text-[1.6vw]']">{{ currentLanguage==='ar' ? secondCategoryArabic : (currentLanguage==='ir' ? secondCategoryPersian : secondCategory) }}</div>
</div>
    </div>
    <div :dir="currentLanguage!=='en' ? 'rtl' : 'ltr'" v-if="products.length>0" class="w-full mb-[5.5vw] grid md:grid-cols-4 grid-cols-2 px-[3.75vw] md:px-[10.8vw] md:mt-[2.7vw] mt-[6.5vw] md:gap-[1.5vw] gap-[0.8vw]">
        <div @click="openProducts(item.slug)" v-for="(item,index) in products" :key="index" class="border-[1px] my-[0.8vw] relative cursor-pointer rounded-[3vw] md:rounded-[0.8vw] border-[#D9C6CB] w-[44.6vw] md:w-[17.6vw] md:h-[17.6vw] h-[44.6vw]">
           <SkeletonLoading :class="['w-full absolute inset-0 h-[31.6vw] md:h-[13vw] rounded-[1vw] md:rounded-[0.8vw]', imagesLoaded[index]===true? 'opacity-0' : 'opacity-100']"/>
           <NuxtImg :src="item.image_url" @load="loadImage(index)" :class="[' absolute inset-0 transition-opacity duration-200 pointer-events-none',imagesLoaded[index]===true ? ' opacity-100 w-full md:h-[13vw] h-[31.6vw]':'h-0 w-0 opacity-0']"/>
           <div :class="['w-full text-[3.7vw] md:text-[1.1vw] text-center md:mt-[1.1vw] mt-[3.7vw]', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">{{ currentLanguage==='ar' ? item.title_arabic : (currentLanguage==='ir' ? item.title_persian : item.title) }}</div>
        </div>
    </div>
    <div v-else class="h-[88vw] md:h-[36vw] w-full flex justify-center items-center">
            <div :class="['opacity-15 text-[7vw] md:text-[5vw] text-center', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat')]">{{ t('noProducts') }}</div>
        </div>
    </div>
</template>

<script>
import SkeletonLoading from '~/components/global/SkeletonLoading.vue';
import { loadingStore } from '~/store/loading-state';
import { categoryStore } from '~/store/category-state.js';
export default{
    data(){
        return {
            categoryState : categoryStore(),
            loadingStore: loadingStore(),
            imagesLoaded:[],
            products:[
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/vJ8xyLq/942b864ebf573bcb3143346c64daa70b-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-ci.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/3s0LV7F/ff0d1418e2ac4be5b0c1108fb531a75a-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-Ch6.png',
                // },
                // {
                //     title:'Title',
                //     titleArabic:'عنوان',
                //     imageUrl:'https://i.ibb.co/0G64kQR/cdb9f1199c899cdcd4da1a93f57ae228-Expires-1731283200-Key-Pair-Id-APKAQ4-GOSFWCVNEHN3-O4-Signature-k-X.png',
                // },
            ],
        }
    },
    components:{
        SkeletonLoading
    },

    setup(){
        const { t, locale } = useI18n();
        const currentLanguage = computed(() => locale.value);
        return {t,currentLanguage}
    },
    computed:{
        firstCategory(){
            return this.categoryState.firstCategory
        },
        secondCategory(){
            return this.categoryState.secondCategory
        },
        firstCategoryArabic(){
            return this.categoryState.firstCategoryArabic
        },
        secondCategoryArabic(){
            return this.categoryState.secondCategoryArabic
        },
        firstCategoryPersian(){
            return this.categoryState.firstCategoryPersian
        },
        secondCategoryPersian(){
            return this.categoryState.secondCategoryPersian
        },
        filter(){
            return this.categoryState.filter;
        }
    },
    mounted(){
        for(let a=0;a<this.products.length;a++){
            this.imagesLoaded.push(false)
        }
        useHead({
      title: this.t('jahanExport') + " | " + this.t('products')
    });
    },
    watch:{
        filter(oldValue,newValue){
            this.fetchProducts()
        }
    },
    created(){
        this.fetchProducts()
        this.loadingStore.setLoading(true)
        this.categoryState.setFirstCategory('Products')
        this.categoryState.setFirstCategoryPersian('محصولات')
        this.categoryState.setSecondCategoryPersian('')
        this.categoryState.setSecondCategory('')
        this.categoryState.setFirstCategoryArabic('منتجات')
        this.categoryState.setSecondCategoryArabic('')
    },
    methods:{
        loadImage(index){
            this.imagesLoaded[index] = true;
        },
        openProducts(productId){
            this.$router.push(`/productDetail/${productId}`);
        },
        fetchProducts(){
            this.loadingStore.setLoading(true)
            this.products = [];
            if(this.categoryState.filter ===''){
                fetch('https://admin.jahanexport.com/products/') 
      .then(response => response.json())
      .then(data => {
        this.products = data;
        this.loadingStore.setLoading(false);
      })
      .catch(error => {
        this.loadingStore.setLoading(false);
        console.error('Error fetching data:', error);
         this.$router.push('/notFound');
      });
            }else{
                fetch('https://admin.jahanexport.com/products/categories/' + this.categoryState.filter + '/') 
      .then(response => response.json())
      .then(data => {
        this.products = data;
        this.loadingStore.setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
         this.$router.push('/notFound');
        this.loadingStore.setLoading(false);
      });
            }
        }
    }
}

</script>