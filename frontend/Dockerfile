# Use the latest LTS version of Node.js
FROM node:lts-alpine

# Set environment to production
ENV NODE_ENV production

# Set working directory for the application
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to leverage Docker cache
COPY ./frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY ./frontend .

# Build the Nuxt application (generate .output directory with nitro.json)
RUN npm run build  # Or nuxi build

# Expose port 3000 for the frontend application
EXPOSE 3000

# Command to run the production server
CMD ["npm", "start"]  # Or nuxi start
