<template>
<div id="app">

<Navbar></Navbar>

<Table></Table>

<Search></Search>

<!-- <Button></Button> -->

<!-- <Pagination></Pagination> -->

<!-- <Getdata></Getdata> -->

</div>
</template>

<script>
import Navbar from './components/Navbar'
import Table from './components/Table'
// import Button from './components/Button'
// import Search from './components/Search'

export default {
  components: {
    Navbar, Table 
    } , 
  data(){
    return{

    }
  }
  
}
</script>




<style scoped>

</style>