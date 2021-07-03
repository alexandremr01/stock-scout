<template>
  <div>
    <h1>{{$t('simulations')}}</h1>

    {{$t('simulationDescription')}}
    <b-container>
      <b-row class="my-1" >
        <b-form-radio v-model="selected" name="some-radios" value="A"/>
        <b-col sm="3" align="left">
          <label>{{$t('initial')}}</label>
        </b-col>
        <b-col sm="4">
          <b-form-input v-model="values.initial" :readonly="selected==='A'" :formatter="currencyFormat" @input="update"></b-form-input>
        </b-col>
      </b-row>
<!--      <b-row class="my-1" >-->
<!--        <b-form-radio v-model="selected" name="some-radios" value="B"/>-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('monthly')}}</label>-->
<!--        </b-col>-->
<!--        <b-col sm="4">-->
<!--          <b-form-input v-model="values.monthly" :readonly="selected==='B'" :formatter="currencyFormat" @input="update"></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
      <b-row class="my-1" >
        <b-form-radio v-model="selected" name="some-radios" value="C"/>
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
        <b-form-radio v-model="selected" name="some-radios" value="E"/>
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
<script>
import i18n from '@/plugins/i18n';

export default {
  name: 'Simulations',
  data () {
    return {
      dialog: false,
      selected: 'E',
      values: {
        initial: null,
        monthly: '0',
        time: null,
        interest: '6.00',
        final: null
      }
    }
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
      if (this.selected === 'E') {
        if (this.values.initial == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let ratio = (1+interest)**(this.values.time/12);
        let final = initial * ratio + monthly*(ratio-1)/(interest);
        this.values.final = this.toCurrency(final);
      } else if (this.selected === 'A') {
        if (this.values.final == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let ratio = (1+interest)**(this.values.time/12);
        let init = (finalValue - monthly*(ratio-1)/(interest))/ratio;
        this.values.initial = this.toCurrency(init);
      } else if (this.selected === 'B') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.time == null)
          return;
        let ratio = (1+interest)**(this.values.time/12);
        let monthly = ((finalValue - initial*ratio) * (ratio) + 1)/ratio;
        this.values.monthly = this.toCurrency(monthly);
      } else if (this.selected === 'C') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.monthly == null)
          return;
        let x = (finalValue + monthly/interest) / (initial + monthly/interest);
        let time = Math.log(x) / Math.log(1 + interest);
        this.values.time = Math.ceil(time*12);
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
      return this.toNumber(n)/100;
    }
  },
};
</script>
<style scoped>
</style>