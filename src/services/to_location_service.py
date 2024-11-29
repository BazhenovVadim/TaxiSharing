import asyncio


class To_location_service:
    @staticmethod
    async def process_to_location(to_location: str):
        # Симулируем асинхронную задачу (например, обращение к внешнему API или базе данных)
        await asyncio.sleep(1)  # задержка 1 секунда для имитации асинхронной работы
        return to_location
