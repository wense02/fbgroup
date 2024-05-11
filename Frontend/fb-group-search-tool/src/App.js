import axios from 'axios';

class App extends React.Component {

  state = { details: [], }

  componentDidMount() {

    let data;
    axios.get('http://localhost:8000')
      .then(res => {
        data = res.data;
        this.setState({
          details: data
        });
      })
      .catch(err => { })
  }

  render() {
    return (
      <div>
        <header>Data Generated From Django</header>
        <hr></hr>
        {this.state.details}
      </div>
    )
  }
}






export default App;