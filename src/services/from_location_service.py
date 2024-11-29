import asyncio


class From_location_service:
    @staticmethod
    async def process_from_location(from_location: str):
        # Симулируем асинхронную задачу (например, обращение к внешнему API или базе данных)
        await asyncio.sleep(1)  # задержка 1 секунда для имитации асинхронной работы
        return from_location
