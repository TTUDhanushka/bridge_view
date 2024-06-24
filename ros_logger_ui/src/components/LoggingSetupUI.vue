<template>
  <div class="container">
    <h1>Tower 1: data recording</h1>
    <h3>Available rostopics to record: 0</h3>
    <button @click="startRecording">Start recording</button>
    <button @click="stopRecording">Stop recording</button>
  </div>
</template>

<script>
export default
{
  name: 'LoggingSetupUI',
  methods: {
    startRecording(){
        fetch('http://localhost:5000/start_recording', {method: 'POST'})
    .then(response =>{
        if(response.ok)
        {
            alert('Recording started');
        }
        else
        {
            alert('Failed to start recording');
        }
    })
    .catch(error => {
        console.error('Error starting recording:', error);
        alert('Error starting recording');
    });
  },
  stopRecording(){
    fetch('http://localhost:5000/stop_recording', {method: 'POST'})
  .then(response=>
    {
        if (response.ok)
        {
            alert('Recording stopped');
        }
        else
        {
            alert('Failed to stop recording');
        }
    })
  .catch(error=>{
    console.error('Error stopping recording', error);
    alert('Error stopping recording');
  });
  }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container{
  text-align: center;
  margin-top: 50px;
}
button {
  background-color: #000;
  border: none;
  color: white;
  height: 40px;
  width: 150px;
  margin: 10px;
  padding: 10px 20 px;
  font-size: 14px;
  border-radius: 20px;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
