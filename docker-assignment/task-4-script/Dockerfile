FROM alpine:latest

WORKDIR /app
COPY task_script.sh /app/task_script.sh

# give me permission to run my script
RUN chmod +x /app/task_script.sh

# CMD/ENTRYPOINT/RUN
CMD [ "/app/task_script.sh" ]