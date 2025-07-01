FROM docker.io/library/nginx:alpine

# Copy static files to nginx web root
COPY index.html /usr/share/nginx/html/index.html
COPY admin.html /usr/share/nginx/html/admin.html
COPY config.js /usr/share/nginx/html/config.js
COPY alerta.mp3 /usr/share/nginx/html/alerta.mp3

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
