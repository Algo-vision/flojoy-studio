from typing import Optional

from pydantic import BaseModel


class CameraDevice(BaseModel):
    name: str
    # either the index or the port (e.g /dev/video0)
    id: str | int

class OT2Device(BaseModel):
    name : str
    address: str

class SerialDevice(BaseModel):
    port: str
    description: str
    manufacturer: Optional[str]
    hwid: str


class VISADevice(BaseModel):
    name: str
    address: str
    description: str


class NIDAQmxDevice(BaseModel):
    name: str
    address: str
    description: str


class NIDMMDevice(BaseModel):
    name: str
    address: str
    description: str


class DeviceInfo(BaseModel):
    cameras: list[CameraDevice]
    serialDevices: list[SerialDevice]
    visaDevices: list[VISADevice]
    nidaqmxDevices: list[NIDAQmxDevice]
    nidmmDevices: list[NIDMMDevice]
