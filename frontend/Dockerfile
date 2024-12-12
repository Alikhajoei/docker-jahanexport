# Use the official Node.js image as a base image
ARG NODE_VERSION=20.18.0
FROM node:${NODE_VERSION}-slim as base

# Set the working directory in the container
WORKDIR /usr/src/app

# Set the environment variable
ENV NODE_ENV=production

# Copy package.json and package-lock.json to install dependencies
COPY ./frontend/package*.json ./
RUN npm install

# Copy the rest of the frontend files
COPY ./frontend .

# Build the Nuxt 3 application
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the application by running the server
CMD [ "npm", "run", "start" ]
