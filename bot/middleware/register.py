from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.handlers.mini_app import cmd_menu
from database.methods import UserMethods



class Register(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user = event.from_user
        if not await UserMethods.is_user_exists(user.id):
            return await handler(event, data)
        else:
            UserMethods.add_user(Message.from_user)
            return await cmd_menu(event)