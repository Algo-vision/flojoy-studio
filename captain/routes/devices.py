from fastapi import APIRouter
from captain.utils.logger import logger
from captain.services.hardware import get_device_finder
from captain.types.devices import DeviceInfo, SerialDevice, VISADevice

router = APIRouter(tags=["devices"])


@router.get("/devices")
async def get_devices():
    device_finder = get_device_finder()
    cameras = device_finder.get_cameras()
    serial_devices = device_finder.get_serial_devices()
    visa_devices = device_finder.get_visa_devices()

    return DeviceInfo(
        cameras=cameras,
        serialDevices=serial_devices,
        visaDevices=visa_devices,
    )