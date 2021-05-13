import PhraseRepository from './PhraseRepository';
import TokenRepository from './TokenRepository';

const repositories = {
    'phrase': PhraseRepository,
    'token': TokenRepository
}
export default {
    get: name => repositories[name]
};