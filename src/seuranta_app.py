from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.asyncio import AsyncIOScheduler # type: ignore
from apscheduler.triggers.cron import CronTrigger # type: ignore


class SeurantaApp(FastAPI):
    def __init__(self):
        super().__init__()

        lease_monitor = AsyncIOScheduler()
        lease_monitor.add_job(self.fetch_leases, CronTrigger(second="*/15")) # type: ignore
        lease_monitor.start()

        self.templates = Jinja2Templates(directory="templates")
        self.mount("/static", StaticFiles(directory="static"), name="static")
        self.init_routes()


    async def fetch_leases(self):
        print("Retrieving DHCP leases... (NOT REALLY! Just pretending)")


    def init_routes(self):
        self.add_route("/", route=self.index)


    async def index(self, req: Request) -> Response:
        return self.templates.TemplateResponse(request=req, name="index.html")