// @flow
import * as Zen from 'lib/Zen';
import Query from 'components/visualizations/common/Query/Query';
import { API_VERSION } from 'services/APIService';
import type BarGraphQueryResultData from 'components/visualizations/BarGraphTNG/models/BarGraphQueryResultData';
import type QueryResultSpec from 'models/core/QueryResultSpec';
import type QuerySelections from 'models/core/wip/QuerySelections';
import type { QueryEngine } from 'models/core/QueryResultState/interfaces/QueryEngine';

const ENDPOINT = 'wip/query/bar_graph_tng';

// prettier-ignore
class BarGraphQueryEngine implements QueryEngine<
  QuerySelections,
  Zen.Serialized<BarGraphQueryResultData>,
> {
  run(
    querySelections: QuerySelections,
    queryResultSpec: QueryResultSpec, // eslint-disable-line no-unused-vars
  ): Promise<Zen.Serialized<BarGraphQueryResultData>> {
    return Query.create(
      ENDPOINT,
      querySelections.serializeForQuery(),
      API_VERSION.V2,
    ).run();
  }
}

export default new BarGraphQueryEngine();
