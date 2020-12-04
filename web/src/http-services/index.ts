import { instance } from './instance';

export const Services = {
    getInitPartie: () => instance.get('/init_game'),
    getNext: (infos: any) => instance.post('/next_tour',  infos)
}