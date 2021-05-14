import PhraseRepository from './PhraseRepository';
import TokenRepository from './TokenRepository';
import RegisterRepository from './RegisterRepository'

const repositories = {
    'phrase': PhraseRepository,
    'token': TokenRepository,
    'register': RegisterRepository
}
export default {
    get: name => repositories[name]
};