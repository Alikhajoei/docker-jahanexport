import { defineStore } from 'pinia';

export const footerStore = defineStore('myStore', {
  state: () => ({
    instagram: '',
    whatsapp:'',
    linkedIn:'',
    email:'',
    phoneNumber:'',
    address:'',
    addressArabic:'',
    addressPersian:'',
    mapLocation:'',
    footerCaption:'',
    footerCaptionAr:'',
    footerCaptionIr:'',
  }),
  actions: {
    setInstagram(newMessage) {
      this.instagram = newMessage;
    },
    setWhatsapp(newMessage){
        this.whatsapp = newMessage
    },
    setLinkedin(newMessage){
        this.linkedIn = newMessage
    },
    setEmail(newMessage){
        this.email = newMessage
    },
    setPhoneNumber(newMessage){
        this.phoneNumber = newMessage
    },
    setAddress(newMessage){
        this.address = newMessage
    },
    setArabicAddress(newMessage){
       this.addressArabic = newMessage
    },
    setPersianAddress(newMessage){
       this.addressPersian = newMessage
    },
    setLocation(newMessage){
        this.mapLocation= newMessage
    },
    setFooterCaption(newMessage){
        this.footerCaption = newMessage
    },
    setFooterArabicCaption(newMessage){
        this.footerCaptionAr = newMessage
    },
    setFooterPersianCaption(newMessage){
      this.footerCaptionIr = newMessage
    }
  },
});