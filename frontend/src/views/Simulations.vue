<template>
  <div>
    <h1>{{$t('simulations')}}</h1>

    {{$t('simulationDescription')}}

    <b-row align-h="start">
      <b-col cols="4">
        <v-select class="style-chooser" @input="updateType" :options="calculationOptions" v-model="selectedSim" ></v-select>
      </b-col>
    </b-row>

    <b-container>
      <b-row class="my-1" >
<!--        <b-form-radio v-model="selected" name="some-radios" value="A"/>-->
        <b-col sm="3" align="left">
          <label>{{$t('initial')}}</label>
        </b-col>
        <b-col sm="4">
          <b-form-input v-model="values.initial" :readonly="selected==='A'" :formatter="currencyFormat" @input="update"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1" >
<!--        <b-form-radio v-model="selected" name="some-radios" value="B"/>-->
        <b-col sm="3" align="left">
          <label>{{$t('monthly')}}</label>
        </b-col>
        <b-col sm="4">
          <b-form-input v-model="values.monthly" :readonly="selected==='B'" :formatter="currencyFormat" @input="update"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1" >
<!--        <b-form-radio v-model="selected" name="some-radios" value="C"/>-->
        <b-col sm="3" align="left">
          <label>{{$t('time')}} </label>
        </b-col>
        <b-col sm="2">
          <b-form-input v-model="values.time" :readonly="selected==='C'" type="number" @input="update" ></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1" >
        <b-col sm="3" align="left">
          <label>{{$t('interest')}}</label>
        </b-col>
        <b-col sm="2">
          <b-form-input v-model="values.interest" :readonly="selected==='D'" :formatter="percentageFormat" @input="update"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1" >
<!--        <b-form-radio v-model="selected" name="some-radios" value="E"/>-->
        <b-col sm="3" align="left">
          <label>{{$t('final')}}</label>
        </b-col>
        <b-col sm="4">
          <b-form-input v-model="values.final" :readonly="selected==='E'" :formatter="currencyFormat" @input="update"></b-form-input>
        </b-col>
      </b-row>
    </b-container>
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
import vSelect from 'vue-select'

export default {
  name: 'Simulations',
  components: {
    vSelect
  },
  data () {
    return {
      dialog: false,
      selected: 'E',
      selectedSim: null,
      calculationOptions: [
        {label: this.$t('initial'), code: 'A'},
        {label: this.$t('monthly'), code: 'B'},
        {label: this.$t('time'), code: 'C'},
        {label: this.$t('final'), code: 'E'},
      ],
      values: {
        initial: null,
        monthly: '0',
        time: null,
        interest: '6.00',
        final: null
      }
    }
  },
  mounted(){
    this.selectedSim = this.calculationOptions[0];
  },
  methods: {
    currencyFormat(value){
      return this.toCurrency(this.toNumber(value)/100)
    },
    percentageFormat(value){
      return value.replace(/[^0-9.-]+/g,"");
    },
    update(){
      let initial = (this.selected !== 'A') ? this.fromText(this.values.initial) : null;
      let monthly = (this.selected !== 'B') ? this.fromText(this.values.monthly) : null;
      let interest = (this.selected !== 'D') ? this.fromText(this.values.interest)/100 : null;
      let finalValue = (this.selected !== 'E') ? this.fromText(this.values.final) : null;

      let monthlyInterest = Math.pow(1+interest, 1/12);
      let ratio = monthlyInterest**(this.values.time);

      if (this.selected === 'E') {
        if (this.values.initial == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let final = initial * ratio + monthly*(ratio-1)/(monthlyInterest-1);
        this.values.final = this.toCurrency(final);
      } else if (this.selected === 'A') {
        if (this.values.final == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let init = (finalValue - monthly*(ratio-1)/(monthlyInterest-1))/ratio;
        this.values.initial = this.toCurrency(init);
      } else if (this.selected === 'B') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.time == null)
          return;
        let monthly = ((finalValue - initial*ratio) * (monthlyInterest-1))/(ratio-1);
        this.values.monthly = this.toCurrency(monthly);
      } else if (this.selected === 'C') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.monthly == null)
          return;
        let aux = monthly/(monthlyInterest-1);
        let x = (finalValue + aux) / (initial + aux);
        let time = Math.log(x) / Math.log(monthlyInterest);
        this.values.time = Math.ceil(time);
      }
    },
    toNumber(n){
      return Number(n.replace(/[^0-9-]+/g,""));
    },
    toCurrency(n){
      let currency = i18n.locale === 'pt-br'? 'BRL' : 'USD';
      return Number(n).toLocaleString('pt-BR', {style: 'currency', currency: currency})
    },
    fromText(n){
      if (n == null) return null;
      return this.toNumber(n)/100;
    },
    updateType(v){
      this.selected = v.code;
    }
  },
};
</script>
<style scoped>
</style>