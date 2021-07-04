<template>
  <div>
    <h1>{{$t('wallets')}}</h1>

    <b-container class="bv-example-row bv-example-row-flex-cols">
          <div class="container-fluid">
            <b-table sticky-header="true" no-border-collapse="true" dark hover :items="wallets" :fields="fields">
              <template #cell(actions)="row">
                <b-button variant="primary" size="sm" @click="$router.push('wallets/'+ row.item.id)" class="mr-1">
                  {{ $t('see') }}
                </b-button>
                <b-button variant="danger" size="sm" @click="remove(row.item, row.index, $event.target)" class="mr-1">
                  {{ $t('remove') }}
                </b-button>
              </template>
            </b-table>
          </div>
    </b-container>

    <h3> Criar nova </h3>
    <div class="container-fluid">
      <b-row class="my-1" align-h="start">
        <b-row cols="12">
          <b-col cols="3" align="left">{{$t('name')}} </b-col>
          <b-col cols="6">
            <b-form-input v-model="walletName" placeholder="Nome"></b-form-input>
          </b-col>
          <b-col cols="3">
            <b-button variant="primary" @click="submit">
              {{ $t('save') }}
            </b-button>
          </b-col>
        </b-row>
      </b-row>
    </div>
  </div>
</template>

<style>
.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
  background: #dfe5fb;
  border: none;
  color: #394066;
  text-transform: lowercase;
  font-variant: small-caps;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: #394066;
}
</style>

<script>
import i18n from '@/plugins/i18n';
import Client from "../repositories/Clients/AxiosClient";
export default {
  name: "Wallets",
  mounted(){
    this.fetchStocks()
  },
  data() {
    return {
      day: 0,
      opType: "Buy",
      quantity: 0,
      value: 0,
      walletName: '',
      symbol: '',
      wallets: [],
      fields:[
        {
          key: 'name',
          sortable: true,
          label: "Nome"
        },
        {
          key: 'created_at',
          sortable: true,
          label: "Criada em"
        },
        {
          key: 'actions',
          label: "Ações"
        },
      ]
    }
  },
  methods: {
    submit(){
      const token = this.$store.state.token;
      console.log(this.walletName)
      let {data} = Client(token).post('/api/wallets/', {
        name: this.walletName,
      }).then((response) => {
        this.fetchStocks();
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
    fetchStocks(){
      const token = this.$store.state.token;
      Client(token).get('/api/wallets/', {}).then((response) => {
        this.wallets = response.data;
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
    async remove(item, index, button) {
      const token = this.$store.state.token;
      await Client(token).delete('/api/wallets/' + item.id + '/').then((response) => {
        this.fetchStocks();
      }).catch((error) => {
        console.log(error)
        this.incorrect = true;
      });
    },
  }
};
</script>

<style>
</style>