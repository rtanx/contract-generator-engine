from fastapi import APIRouter, BackgroundTasks, Body, Depends, status

from api.services.contract import ContractService

from .models import ContractConstructor

router = APIRouter()


@router.post('/scaffold-contract', status_code=status.HTTP_201_CREATED)
async def scaffold_contract(constructor_args: ContractConstructor, bg_task: BackgroundTasks, contract_srvc: ContractService = Depends(ContractService)):
    # bg_task.add_task(contract_srvc.scaffold, token_name=constructor_args.token_name, token_symbol=constructor_args.token_symbol, metadata_base_uri=constructor_args.base_uri)
    tx = contract_srvc.scaffold(constructor_args.token_name, constructor_args.token_symbol, constructor_args.base_uri)
    print(tx)
    return {
        'success': True,
        'message': 'contract creation is in progress',
        'tx_hash': tx,
    }


@router.get('/status', status_code=200)
def contract_status():
    pass