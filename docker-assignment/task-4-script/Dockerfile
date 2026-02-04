FROM alpine:latest

WORKDIR /app
COPY task_script.sh /app/task_script.sh
RUN chmod +x /app/task_script.sh

ENTRYPOINT [ "/app/task_script.sh" ]