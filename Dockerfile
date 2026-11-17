FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY . .
RUN mkdir -p out && javac -d out $(find src -name "*.java")
CMD ["sh", "-c", "echo 'Build successful'"]