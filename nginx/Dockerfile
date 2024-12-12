
# # runing nginx and putting in loop
# CMD ["nginx", "-g", "daemon off;"]



# استفاده از Nginx official image
FROM nginx:stable-alpine

# کپی کردن تنظیمات Nginx به داخل کانتینر
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# پورت 80 را باز کنید
EXPOSE 80
