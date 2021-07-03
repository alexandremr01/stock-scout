<template>
  <div>
    <h1>{{$t('simulations')}}</h1>

    {{$t('simulationDescription')}}

    <b-row align-h="start">
      <b-col cols="4">
        <v-select class="style-chooser" @input="updateType" :options="calculationOptions" v-model="selectedSim"></v-select>
      </b-col>
    </b-row>

    <b-container>
      <b-row class="my-1" v-for="input in inputs" :key="input.name">
        <b-col sm="3" align="left">
          <label>{{$t(input.name)}}</label>
        </b-col>
        <b-col sm="4">
          <b-form-input v-model="input.value" :readonly="selected===input.name" :formatter="input.formatter" @input="update"></b-form-input>
        </b-col>
      </b-row>
    </b-container>

<!--    <b-container>-->
<!--      <b-row class="my-1" >-->
<!--&lt;!&ndash;        <b-form-radio v-model="selected" name="some-radios" value="A"/>&ndash;&gt;-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('initial')}}</label>-->
<!--        </b-col>-->
<!--        <b-col sm="4">-->
<!--          <b-form-input v-model="values.initial" :readonly="selected==='A'" :formatter="currencyFormat" @input="update"></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
<!--      <b-row class="my-1" >-->
<!--&lt;!&ndash;        <b-form-radio v-model="selected" name="some-radios" value="B"/>&ndash;&gt;-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('monthly')}}</label>-->
<!--        </b-col>-->
<!--        <b-col sm="4">-->
<!--          <b-form-input v-model="values.monthly" :readonly="selected==='B'" :formatter="currencyFormat" @input="update"></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
<!--      <b-row class="my-1" >-->
<!--&lt;!&ndash;        <b-form-radio v-model="selected" name="some-radios" value="C"/>&ndash;&gt;-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('time')}} </label>-->
<!--        </b-col>-->
<!--        <b-col sm="2">-->
<!--          <b-form-input v-model="values.time" :readonly="selected==='C'" type="number" @input="update" ></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
<!--      <b-row class="my-1" >-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('interest')}}</label>-->
<!--        </b-col>-->
<!--        <b-col sm="2">-->
<!--          <b-form-input v-model="values.interest" :readonly="selected==='D'" :formatter="percentageFormat" @input="update"></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
<!--      <b-row class="my-1" >-->
<!--&lt;!&ndash;        <b-form-radio v-model="selected" name="some-radios" value="E"/>&ndash;&gt;-->
<!--        <b-col sm="3" align="left">-->
<!--          <label>{{$t('final')}}</label>-->
<!--        </b-col>-->
<!--        <b-col sm="4">-->
<!--          <b-form-input v-model="values.final" :readonly="selected==='E'" :formatter="currencyFormat" @input="update"></b-form-input>-->
<!--        </b-col>-->
<!--      </b-row>-->
<!--    </b-container>-->
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
      selected: null,
      selectedSim: null,
      calculationOptions: [
        {label: this.$t('initial'), name: 'initial'},
        {label: this.$t('monthly'), name: 'monthly'},
        {label: this.$t('time'), name: 'time'},
        {label: this.$t('final'), name: 'final'},
      ],
      values: {
        initial: null,
        monthly: '0',
        time: null,
        interest: '6.00',
        final: null
      },
      inputs:[
        {name:'initial', originalIndex: 0, formatter: this.currencyFormat, value: null},
        {name:'monthly', originalIndex: 1, formatter: this.currencyFormat, value: null},
        {name:'time', originalIndex: 2, value: null},
        {name:'interest', originalIndex: 3, formatter: this.percentageFormat, value: '6.0'},
        {name:'final', originalIndex: 4, formatter: this.currencyFormat, value: null},
      ]
    }
  },
  mounted(){
    this.selectedSim = this.calculationOptions[3];
    this.selected = 'final';
  },
  methods: {
    currencyFormat(value){
      return this.toCurrency(this.toNumber(value)/100)
    },
    percentageFormat(value){
      return value.replace(/[^0-9.]+/g,"");
    },
    update(){
      this.inputs.forEach((v, i,a) => this.values[v.name] = v.value)

      let initial = (this.selected !== 'A') ? this.fromText(this.values.initial) : null;
      let monthly = (this.selected !== 'B') ? this.fromText(this.values.monthly) : null;
      let interest = (this.selected !== 'D') ? this.fromText(this.values.interest)/100 : null;
      let finalValue = (this.selected !== 'E') ? this.fromText(this.values.final) : null;

      let monthlyInterest = Math.pow(1+interest, 1/12);
      let ratio = monthlyInterest**(this.values.time);

      if (this.selected === 'final') {
        if (this.values.initial == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let final = initial * ratio + monthly*(ratio-1)/(monthlyInterest-1);
        this.values.final = this.toCurrency(final);
      } else if (this.selected === 'initial') {
        if (this.values.final == null || this.values.interest==null || this.values.monthly == null || this.values.time == null)
          return;
        let init = (finalValue - monthly*(ratio-1)/(monthlyInterest-1))/ratio;
        this.values.initial = this.toCurrency(init);
      } else if (this.selected === 'monthly') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.time == null)
          return;
        let monthly = ((finalValue - initial*ratio) * (monthlyInterest-1))/(ratio-1);
        this.values.monthly = this.toCurrency(monthly);
      } else if (this.selected === 'time') {
        if (this.values.final == null || this.values.interest==null || this.values.initial == null || this.values.monthly == null)
          return;
        let aux = monthly/(monthlyInterest-1);
        let x = (finalValue + aux) / (initial + aux);
        let time = Math.log(x) / Math.log(monthlyInterest);
        this.values.time = Math.ceil(time);
      }
      this.inputs.forEach((v, i,a) => v.value=this.values[v.name])

    },
    toNumber(n){
      return Number(n.replace(/[^0-9]+/g,""));
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
      console.log(this.inputs)
      this.selected = v.name;
      let retIndex = this.inputs[4].originalIndex;
      let bkp = this.inputs[retIndex];
      this.inputs[retIndex] = this.inputs[4];
      this.inputs[4] = bkp;

      let res = this.inputs.find(x => x.name === v.name);
      this.inputs[res.originalIndex] = this.inputs[4];
      this.inputs[4] = res;
      // let res = this.inputs.findIndex(x => x.code === v.code);
      // let cutOut = this.inputs.splice(res, 1) [0]; // cut the element at index 'from'
      // this.inputs.splice(5, 0, cutOut);            // insert it at index 'to'
    }
  },
};
</script>
<style scoped>
</style>