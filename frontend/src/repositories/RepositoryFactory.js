import PhraseRepository from './PhraseRepository';

const repositories = {
    'phrase': PhraseRepository
}
export default {
    get: name => repositories[name]
};