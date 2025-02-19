from database import new_session, TaskOrm
from schemas import STaskAdd
from sqlalchemy import select

from schemas import STask

class TaskRepository():
    @classmethod
    async def add_one(cls, data:STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()
        
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flusk()
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
              query = select()
              result = await session.execute(query)
              task_models = result.scalar().all()
              task_schemas = [STask.model_validate(task_model) for task_model in task_models]
              return task_models
