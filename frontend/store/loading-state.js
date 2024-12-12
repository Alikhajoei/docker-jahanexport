import { defineStore } from 'pinia';

export const loadingStore = defineStore('loadingStore', {
    state: () => ({
        isLoading:false,
      }),
      actions: {
        setLoading(newMessage) {
          this.isLoading = newMessage;
        },
        disableLoading(){
          this.isLoading = false;
        }
    }
});