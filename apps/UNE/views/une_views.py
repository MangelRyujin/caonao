from django.shortcuts import render
from apps.UNE.models import Affectation, Block, Circuit


# Create View UNE Table
def une_view(request):
    blocks = Block.objects.filter(active= True)
    affectation= Affectation.objects.filter(
        active = True
    ).order_by('in_date','in_time')
    block_circuit = []
    for block in blocks:
       block_circuit.append({
           'block': block.name,
           'circuit': Circuit.objects.filter(block=block).exclude(active=False)
       })
    context = {'block': block_circuit, 'affectation': affectation}
    return render(request,'une_view.html',context)
