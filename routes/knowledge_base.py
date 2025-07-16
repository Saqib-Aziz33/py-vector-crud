from fastapi.routing import APIRouter

router = APIRouter()


@router.get('/')
def get_all_knowledge_base():
    return "knowledge base implementation"


@router.post('/')
def get_all_knowledge_base():
    return "new knowledge base implementation"


@router.get("/{item_id}")
def get_knowledge_base_item(item_id: str):
    return "single item implementation"


@router.delete("/{item_id}")
def delete_knowledge_base_item(item_id: str):
    return "single item implementation"
