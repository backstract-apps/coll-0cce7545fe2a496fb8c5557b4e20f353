from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class AppointmentTypes(BaseModel):
    id: Any
    name: str
    duration: int
    description: str


class ReadAppointmentTypes(BaseModel):
    id: Any
    name: str
    duration: int
    description: str
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    user_id: int
    appointment_type_id: int
    datetime: Any


class ReadAppointments(BaseModel):
    id: Any
    user_id: int
    appointment_type_id: int
    datetime: Any
    class Config:
        from_attributes = True




class PostAppointmentTypes(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    duration: int = Field(...)
    description: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    id: int = Field(...)
    user_id: int = Field(...)
    appointment_type_id: int = Field(...)
    datetime: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

