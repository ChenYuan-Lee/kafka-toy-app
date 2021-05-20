The following instructions are partly obtained from: https://docs.confluent.io/platform/current/quickstart/ce-quickstart.html#ce-quickstart

# Setup
1. Install Java (this worked for me: https://java.com/en/download/)
2. Download Confluent Platform: https://www.confluent.io/download/?_ga=2.124058184.397616571.1621250059-1943697987.1618994787&_gac=1.94586478.1621264796.CjwKCAjwqIiFBhAHEiwANg9szhZyjB7kj_mBswZeuGh7KLTJn5EISsJlgxxXMFC0RY2CNs3JevZF6BoCYREQAvD_BwE
2. Assuming you're using **oh my zsh**, can add `source ~/.bash_profile` line at the end of `.zshrc` file at the following
   path: `/Users/YOUR USER NAME/.zshrc`. Add the following into your `~/.bash_profile`:
   ```
   export CONFLUENT_HOME=<path-to-confluent>
   export PATH=$PATH:$CONFLUENT_HOME/bin
   ```
3. Run `confluent local services start`
4. Run `pip install -r requirements.txt` to install required Python dependencies

# Usage
* Run `producer.py` to produce data
* Run `consumer.py` to consume data
* Refer to `avro_schemas` folder to adjust key and value schemas
* View topics and messages @ http://localhost:9021/clusters

# Termination
* Run `confluent local services stop` to terminate
* Run `confluent local destroy` to destroy data in the Confluent Platform instance
