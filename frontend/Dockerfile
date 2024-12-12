# مرحله اول: مرحله ساخت (Build Stage)
FROM node:20.18.0-slim as build

# تنظیم محیط به production
ENV NODE_ENV production

# تنظیم دایرکتوری کاری
WORKDIR /usr/src/app

# کپی کردن فایل‌های پکیج برای نصب وابستگی‌ها
COPY ./frontend/package*.json ./

# نصب وابستگی‌ها
RUN npm install

# کپی کردن تمام کد برنامه
COPY ./frontend .

# ساخت پروژه برای حالت تولید
RUN npm run build

# مرحله دوم: مرحله اجرای (Run Stage)
FROM node:20.18.0-slim as base

# تنظیم محیط به production
ENV NODE_ENV production

# تنظیم دایرکتوری کاری
WORKDIR /usr/src/app

# کپی کردن فایل‌های ساخته‌شده از مرحله build
COPY --from=build /usr/src/app/.output /usr/src/app/.output

# پورت مورد استفاده برای برنامه
EXPOSE 3000

# اجرای پروژه از فایل .output
CMD [ "node", ".output/server/index.mjs" ]
