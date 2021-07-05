<template>
  <div class="big-box-wallet">
    <b-container class="small-box">
      <b-container fluid class="title-wallet">
        <h1 class="text-secondary">{{$t('wallets')}}</h1>
      </b-container>

      <b-container fluid class="wallet-list bg-secondary text-primary">
              <b-table 
                sticky-header="true" 
                no-border-collapse dark hover 
                :items="wallets" 
                :fields="fields"
                >
                <template #cell(actions)="row">
                  <b-button
                    pill 
                    variant="primary" 
                    size="sm" 
                    @click="$router.push('wallets/'+ row.item.id)" 
                    class="mr-1 text-dark"
                    >
                    {{ $t('see') }}
                  </b-button>
                  <b-button
                    pill 
                    variant="danger" 
                    size="sm" 
                    @click="remove(row.item, row.index, $event.target)" 
                    class="mr-1"
                    >
                    {{ $t('remove') }}
                  </b-button>
                </template>
              </b-table>
      </b-container>
    </b-container>


    <b-container fluid class="pt-5 title-wallet">
      <h2 class="text-secondary">{{ $t('createNew') }}</h2>
    </b-container>

    <div class="container-fluid">
      <b-row class="my-1" align-h="center">
        <b-row cols="12">
          <b-col cols="3" align-self="center"><h3 class="text-dark">{{$t('name')}}</h3></b-col>
          <b-col cols="6">
            <b-form-input v-model="walletName" placeholder="Nome"></b-form-input>
          </b-col>
          <b-col cols="3">
            <b-button pill variant="primary" @click="submit" class="text-dark">
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
.title-wallet {
  padding: 10px;
}
.big-box-wallet {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
}
.wallet-list {
  padding: 20px;
  max-width: 50%;
  height: auto;
  border-radius: 20px;
}
.small-box {
  display: flex;
  flex-direction: column;
  justify-content: start;
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
          label: this.$t("name")
        },
        {
          key: 'created_at',
          sortable: true,
          label: this.$t("created_at")
        },
        {
          key: 'actions',
          label: this.$t("actions")
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
