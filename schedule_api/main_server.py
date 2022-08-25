from fastapi import FastAPI

import config
import information


app = FastAPI(
  title=information.title,
  description=information.description,
  version=information.version,
  contact=information.contact,
  license_info=information.license_info,
  root_path=config.root_path)


@app.on_event('startup')
async def startup_event():
    pass


@app.on_event('shutdown')
async def shutdown_event():
    pass

