from flask.ext.moment import Moment

import magnum


Moment(magnum.app)

magnum.app.run(debug=True)
