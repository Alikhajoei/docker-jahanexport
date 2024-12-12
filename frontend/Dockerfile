# Use the latest LTS version of Node.js
FROM node:lts-alpine

# Set environment to development
ENV NODE_ENV development

# Set working directory for the application
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json to leverage Docker cache
COPY ./app/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY ./app .

# Expose port 3000 for the frontend application
EXPOSE 3000

# Command to run the development server
CMD ["npm", "start"]
