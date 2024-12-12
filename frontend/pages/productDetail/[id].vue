<template>
    <div>
        <div class="w-full h-[10vw] md:h-[5.5vw]"></div>
        <div class="flex  flex-col md:flex-row  w-full mb-[2.8vw] ">
            <div class="basis-1/2">
                <div class="flex justify-center select-none items-center">
                    <svg @click="previousSlide"
                        class="w-[15vw] rotate-180 h-[15vw] md:h-[4.8vw] md:w-[4.8vw] cursor-pointer"
                        viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M18.7148 28.0078L34.6523 12.0703C35.7539 10.9688 37.5352 10.9688 38.625 12.0703L41.2734 14.7187C42.375 15.8203 42.375 17.6016 41.2734 18.6914L29.9883 30L41.2852 41.2969C42.3867 42.3984 42.3867 44.1797 41.2852 45.2695L38.6367 47.9297C37.5352 49.0312 35.7539 49.0312 34.6641 47.9297L18.7266 31.9922C17.6133 30.8906 17.6133 29.1094 18.7148 28.0078Z"
                            fill="#791A4D" />
                    </svg>
                    <div class="w-full md:w-[31.25vw] flex relative justify-center items-center md:h-[20.8vw] h-[65.11vw]">
                        <SkeletonLoading
                            :class="['w-full h-full md:rounded-[0.3vw] absolute inset-0', imageLoaded ? 'opacity-0':' opacity-100']" />
                        <NuxtImg @load="loadImage"
                            :class="['transition-opacity md:rounded-[0.3vw] absolute inset-0 object-fill duration-150', imageLoaded ? 'h-full  w-full opacity-100' : 'h-0 w-0 opacity-0']"
                            :src="currentImage" loading="lazy"/>
                    </div><svg @click="nextSlide" class="w-[15vw] rot h-[15vw] md:h-[4.8vw] md:w-[4.8vw] cursor-pointer"
                        viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M18.7148 28.0078L34.6523 12.0703C35.7539 10.9688 37.5352 10.9688 38.625 12.0703L41.2734 14.7187C42.375 15.8203 42.375 17.6016 41.2734 18.6914L29.9883 30L41.2852 41.2969C42.3867 42.3984 42.3867 44.1797 41.2852 45.2695L38.6367 47.9297C37.5352 49.0312 35.7539 49.0312 34.6641 47.9297L18.7266 31.9922C17.6133 30.8906 17.6133 29.1094 18.7148 28.0078Z"
                            fill="#791A4D" />
                    </svg>
                </div>
                <div class="w-[100vw] md:w-full md:mt-[1.6vw] mt-[5.5vw] md:px-[8.55vw] px-[3.75vw]">
                    <div class="w-full h-[33vw] md:h-[8.75vw] flex justify-between">
                        <div @click="setImage(index)"
                            class="w-[28vw] md:w-[10.4vw] mx-[0.7vw] cursor-pointer bg-white border-[1px] border-[#D9C6CB] md:p-[0.3vw] p-[1vw] h-[28vw] md:h-[8.75vw] md:rounded-[0.8vw] rounded-[3vw]"
                            v-for="(image, index) in images" :key="index">
                            <div class="w-full h-full relative">
                                <NuxtImg @load="loadSliderImage(index)" :src="image" :class="['rounded-[3vw] md:rounded-[0.8vw] object-fill h-full w-full absolute inset-0 transition-opacity duration-200', imagesLoaded[index]===true? 'opacity-100 w-full h-full' : 'opacity-0 w-0 h-0']" />
                                <SkeletonLoading :class="['rounded-[3vw] md:rounded-[0.8vw] object-fill h-full w-full absolute inset-0 transition-opacity duration-200', imagesLoaded[index]===false ? 'opacity-100 h-full w-full' : 'opacity-0 h-0 w-0']" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="basis-1/2">
                <h1
                    :class="['text-center md:text-[2.2vw] md:mt-0 mt-[7.4vw] md:mb-[2.2vw] text-[7.4vw]', currentLanguage==='ar' ? 'cairo' : (currentLanguage==='ir' ? 'vazir' : 'montserrat') ,currentLanguage !== 'en' ? ' md:text-right' : 'pl-[10.8vw] md:text-left ']">
                    {{ currentLanguage === 'ar' ? titleArabic : (currentLanguage==='ir' ? titlePersian : title)  }}</h1>
                <div :class="[currentLanguage !== 'en' ? 'rtl-justify' : 'text-left']">
                    <div :class="['md:text-[1.1vw] md:pl-[10.8vw] pl-[3.75vw] pr-[3.75vw] md:pr-0 ', currentLanguage === 'ar' ? 'cairo ' : (currentLanguage==='ir' ? 'vazir': 'montserrat')]"
                        v-html="currentLanguage === 'ar' ? contentArabic : (currentLanguage==='ir'? contentPersian : content)"></div>
                    <div
                        :class="['w-full  flex justify-center md:pl-[10.8vw] pl-0 items-center md:mt-[3.3vw] mt-[6.5vw] mb-[9.3vw]',currentLanguage!=='en' ? 'md:justify-start':'md:justify-end']">
                        <NuxtLink to="/contactUs"
                            class="w-[40.4vw] md:w-[12vw] bg-[#791A4D] md:py-[0.7vw] py-[2.3vw] transition-all duration-200 rounded-full flex cursor-pointer hover:bg-[#4e1534] justify-center items-center">
                            <div :class="[currentLanguage === 'ar' ? 'cairo' : (currentLanguage==='ir'?'vazir' : 'montserrat'), 'text-white']">{{
                                t('order') }}</div>
                        </NuxtLink>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script>
import { loadingStore } from '~/store/loading-state';
import SkeletonLoading from '~/components/global/SkeletonLoading.vue';
export default {
    setup() {
        const { t, locale } = useI18n();
        const currentLanguage = computed(() => locale.value);
        return {
            t,
            currentLanguage,
        };
    },
    components:{
        SkeletonLoading,
    },
    data() {
        return {
            loadingState:loadingStore(),
            currentSlide: 0,
            title: '',
            titleArabic: '',
            titlePersian:'',
            content: '',
            contentArabic: '',
            contentPersian:'',
            images: [
              ],
            currentImage: '',
            imageLoaded: false,
            imagesLoaded:[],
        }
    },
    methods: {
        async fetchProductData(){
            this.loadingState.setLoading(true)
            const productId = this.$route.params.id; 

            try {
        const response = await fetch(`https://admin.jahanexport.com/products/${productId}/`); 
        if (!response.ok) {
            this.$router.push('/notFound');
          throw new Error('Failed to fetch product data');
        }
        const data = await response.json();
        this.title = data.title;
        this.titleArabic = data.title_arabic; 
        this.titlePersian = data.title_persian;
        this.currentImage = data.image_url;
        this.images.push(this.currentImage);
        for(let a=0; a< data.extra_images.length;a++){
            this.images.push(data.extra_images[a]);
        }
        this.loadingState.setLoading(false)
        this.content = data.caption;
        this.contentArabic = data.caption_arabic
        this.contentPersian = data.caption_persian;
        for(let a=0; a< this.images.length;a++){
            this.imagesLoaded.push(false);
        }
      } catch (err) {
                    this.loadingState.setLoading(false)
        this.error = err.message; 
        this.$router.push('/notFound');
      } finally {
                    this.loadingState.setLoading(false)
        this.loading = false; 
      }
        },
        nextSlide() {
            if (this.currentSlide < this.images.length - 1) {
                this.currentSlide++;
                this.imageLoaded = false;
                this.currentImage = this.images[this.currentSlide]
            }
        },
        previousSlide() {
            if (this.currentSlide > 0) {
                this.currentSlide--;
                this.imageLoaded = false;
                this.currentImage = this.images[this.currentSlide];
            }
        },
        loadImage() {
            this.imageLoaded = true;
        },
        setImage(index) {
            this.currentSlide = index;
            this.currentImage = this.images[this.currentSlide];
        },
        loadSliderImage(index){
            this.imagesLoaded[index] = true;
        }
    },
    mounted() {
        this.currentImage = this.images[this.currentSlide]
        useHead({
      title: this.t('jahanExport') + " | " + this.t('productDetail')
    });
    },
    created(){
       this.loadingState.setLoading(true);
       this.fetchProductData()
    },
    computed:{
        isProductDetailPage() {
      return this.$route.path.startsWith('/productDetail');
    }
    },
}
</script>