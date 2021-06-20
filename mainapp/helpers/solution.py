def solution(request):
    request.session['round'] = request.session.get('round', 0)
    request.session['remaining'] = [0] * request.session['areaNumber']
    print('Areas ', request.session['areas'] )
    if not any(request.session['areas']):
        return
    if request.session['vanNumber'] == 1:
        for i in range(request.session['areaNumber']):
            before = list(request.session['areas'])
            if request.session['areas'][i] == 0:
                print('zero ', i)
                continue
            if request.session['count'][i] == 1:
                request.session['wastage'][i] += request.session['doseNumber'] - request.session['areas'][i]
                request.session['areas'][i] = 0
                request.session.modified = True
                continue
            if request.session['areas'][i] <= request.session['doseNumber']:
                request.session['count'][i] += 1
                continue
            if request.session['areas'][i] >= request.session['doses'][i]:
                request.session['areas'][i] -= request.session['doses'][i]
            if request.session['areas'][i] < request.session['doses'][i]:
                request.session['areas'][i] = request.session['areas'][i] % request.session['doseNumber']
            request.session['remaining'][i] = (int(before[i] - request.session['areas'][i]))
            request.session.modified = True
        request.session['round'] += 1
        request.session['total_waste'] = sum(request.session['wastage'])
        print('After', request.session['areas'], '\n')
    else:
        pass
    return
