<template>
  <div class="outercontainer">
    <div class="aboutcard bg-secondary">
      <div class="toptext">
        <h1 class="made text-primary">{{ $t("madeBy") }}</h1>
      </div>
      <div class="middletext">
        <h5 class="credits">Alexandre Maranhão</h5>
        <h5 class="credits">Alvaro Tedeschi</h5>
        <h5 class="credits">Davi Vasconcelos</h5>
        <h5 class="credits">Gabriel Teixeira</h5>
        <h5 class="credits">Kenji Yamane</h5>
      </div>
      <div class="toptext"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "About",
};
</script>
<style scoped>
.outercontainer {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  align-content: center;
}
.aboutcard {
  width: 50%;
  height: 50%;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.toptext {
  width: 100%;
  height: 20%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.middletext {
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.made {
  font-size: 3vw;
}

.credits {
  font-size: 1.8vw;
}
</style>