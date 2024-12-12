# Use the latest LTS version of Node.js
FROM node:lts-alpine

# Set environment to development or production (can be overridden in Docker Compose)
ARG NODE_ENV=development
ENV NODE_ENV ${NODE_ENV}

# Set working directory for the application
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json to leverage Docker cache
COPY ./frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY ./frontend .

# If in development, use the dev server. In production, build and then start.
RUN if [ "$NODE_ENV" = "production" ]; then npm run build; fi
RUN npx nuxi build 
# Expose port 3000 for the frontend application
EXPOSE 3000

# Command to run the development server (default)
# CMD ["npm", "run", "dev"]

# Production command (uncomment the next line if you want to default to production)
CMD ["npm", "run", "start"]
