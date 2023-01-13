# honeygain-daily
Automatically claim the daily honeypot  
There is a crontab that will run the included python script at 10pm.

## Example
docker run --name honeygain-daily -d  -e JWT_TOKEN=<-!your token!-> -e DISCORD_WEBHOOK=<-!channel webhook!-> ziggyds/honeygain-daily

[https://hub.docker.com/r/ziggyds/honeygain-daily](https://hub.docker.com/r/ziggyds/honeygain-daily)
