Basic dropdown, with a "Select All" option:
```jsx
initialState = {
  value: [],
};

function onSelectionChange(value) {
  setState({ value });
}

<Dropdown.Multiselect
  value={state.value}
  onSelectionChange={onSelectionChange}
  defaultDisplayContent="Make a selection"
  enableSelectAll
>
  <Dropdown.Option value="First">
    First option!
  </Dropdown.Option>
  <Dropdown.Option value="Second">
    Second option!
  </Dropdown.Option>
</Dropdown.Multiselect>
```

Dropdown with searchable items. For demonstration purposes, the fourth item in this dropdown is configured so that it is both unselectable and unaffected by the search text.
You can also pass a `renderButtonLabel` prop to render the button contents in a more customized way:
```jsx
initialState = {
  value: ["Active"],
};

function onSelectionChange(value) {
  setState({ value });
}

// NOTE(pablo): the empty array case must be handled through
// `defaultDisplayContent`. This function will never receive an empty array.
function renderButtonLabel(values) {
  return (
    <React.Fragment>
      {values.join(', ')} <strong>({values.length})</strong>
    </React.Fragment>
  );
}

const options = ["Active", "Pending", "Some other status"];
const optionItems = options.map(optString => (
  <Dropdown.Option
    key={optString}
    value={optString}
    searchableText={optString}
  >
    {optString}
  </Dropdown.Option>
));

<Dropdown.Multiselect
  enableSearch
  enableSelectAll
  value={state.value}
  onSelectionChange={onSelectionChange}
  menuMinWidth={400}
  renderButtonLabel={renderButtonLabel}
  defaultDisplayContent="No selections made"
>
  {optionItems}
  <Dropdown.Option value="Unselectable!" disableSearch unselectable>
    Unselectable!
  </Dropdown.Option>
</Dropdown.Multiselect>
```

Dropdowns can nest their options into groups, and you can still have everything be searchable:
```jsx
initialState = {
  value: [],
};

function onSelectionChange(value) {
  setState({ value });
}

const myDashboards = ['Amazing Dashboard', 'Something Important'];
const otherDashboards = ["Quentin's Dashboard", "Nina's Analysis", 'Wow another option'];
const myDashboardOptions = myDashboards.map(dash =>
  <Dropdown.Option
    key={dash}
    value={dash}
    searchableText={dash}
  >
    {dash}
  </Dropdown.Option>
);
const otherDashboardOptions = otherDashboards.map(dash =>
  <Dropdown.Option
    key={dash}
    value={dash}
    searchableText={dash}
  >
    {dash}
  </Dropdown.Option>
);

<Dropdown.Multiselect
  enableSearch
  value={state.value}
  onSelectionChange={onSelectionChange}
  menuMinWidth={400}
  defaultDisplayContent="Choose a Dashboard"
>
  <Dropdown.OptionsGroup
    id="my-dashboards"
    label="My Dashboards"
    searchableText="My Dashboards"
  >
    {myDashboardOptions}
  </Dropdown.OptionsGroup>
  <Dropdown.OptionsGroup
    id="other-dashboards"
    label="Other Dashboards"
    searchableText="Other Dashboards"
  >
    {otherDashboardOptions}
  </Dropdown.OptionsGroup>
</Dropdown.Multiselect>
```

Dropdowns with left and right menu alignments:
```jsx
initialState = {
  firstValue: [],
  secondValue: [],
};

function onSelectionChange1(value) {
  setState({ firstValue: value });
}

function onSelectionChange2(value) {
  setState({ secondValue: value });
}

<React.Fragment>
  <Dropdown.Multiselect
    value={state.firstValue}
    onSelectionChange={onSelectionChange1}
    defaultDisplayContent="Left alignment"
    menuAlignment={Dropdown.Alignments.LEFT}
  >
    <Dropdown.Option value="First">
      First option with some longer text to show off the menu alignment
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option!
    </Dropdown.Option>
  </Dropdown.Multiselect>

  <Dropdown.Multiselect
    value={state.secondValue}
    onSelectionChange={onSelectionChange2}
    defaultDisplayContent="Right alignment"
    menuAlignment={Dropdown.Alignments.RIGHT}
  >
    <Dropdown.Option value="First">
      First option with some longer text to show off the menu alignment
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option!
    </Dropdown.Option>
  </Dropdown.Multiselect>
</React.Fragment>
```

You can control the dropdown button width using `buttonWidth` and `buttonMinWidth`.
Notice how in the first dropdown, if you make a selection that extends past the `buttonWidth` then we will add an elipsis to cut off the text:
```jsx
import LabelWrapper from 'components/ui/LabelWrapper';

initialState = {
  firstValue: [],
  secondValue: [],
  thirdValue: [],
};

function onSelectionChange1(value) {
  setState({ firstValue: value });
}

function onSelectionChange2(value) {
  setState({ secondValue: value });
}

function onSelectionChange3(value) {
  setState({ thirdValue: value });
}

<React.Fragment>
  <Dropdown.Multiselect
    value={state.firstValue}
    onSelectionChange={onSelectionChange1}
    defaultDisplayContent="200px button width"
    buttonWidth={200}
  >
    <Dropdown.Option value="First">
      First option with some long text that extends past this dropdown's button width
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option with some long text that extends past this dropdown's button width
    </Dropdown.Option>
  </Dropdown.Multiselect>

  <Dropdown.Multiselect
    value={state.secondValue}
    onSelectionChange={onSelectionChange2}
    defaultDisplayContent="200px min width"
    buttonMinWidth={200}
  >
    <Dropdown.Option value="First">
      First option with some longer text to show off the menu alignment
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option!
    </Dropdown.Option>
  </Dropdown.Multiselect>

  <LabelWrapper label="Dropdown with 100% width">
    <Dropdown.Multiselect
      value={state.thirdValue}
      onSelectionChange={onSelectionChange3}
      defaultDisplayContent="Button with 100% width!"
      buttonWidth="100%"
    >
      <Dropdown.Option value="First">
        First option with some longer text to show off the menu alignment
      </Dropdown.Option>
      <Dropdown.Option value="Second">
        Second option!
      </Dropdown.Option>
    </Dropdown.Multiselect>
  </LabelWrapper>
</React.Fragment>
```

Use `menuWidth` or `menuMinWidth` to control the width of the menu. You can set an exact pixel width, or you can use a string if you wanted to set a percentage width. The percentage width will be calculated based off of the button. E.g. `width="50%"` will create a menu with 50% of the button width. `width="100%"` will make the menu's width be the same as the button's.
```jsx
import LabelWrapper from 'components/ui/LabelWrapper';

initialState = {
  firstValue: [],
  secondValue: [],
  thirdValue: [],
};

function onSelectionChange1(value) {
  setState({ firstValue: value });
}

function onSelectionChange2(value) {
  setState({ secondValue: value });
}

function onSelectionChange3(value) {
  setState({ thirdValue: value });
}

<React.Fragment>
  <Dropdown.Multiselect
    value={state.firstValue}
    onSelectionChange={onSelectionChange1}
    defaultDisplayContent="50% menu min width"
    buttonWidth={300}
    menuMinWidth="50%"
  >
    <Dropdown.Option value="First">
      First
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second
    </Dropdown.Option>
  </Dropdown.Multiselect>

  <Dropdown.Multiselect
    value={state.secondValue}
    onSelectionChange={onSelectionChange2}
    defaultDisplayContent="100% menu width"
    buttonWidth={300}
    menuWidth="100%"
  >
    <Dropdown.Option value="First">
      First option with long text to show off how long options break into multiple lines when the menu has fixed width
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option!
    </Dropdown.Option>
  </Dropdown.Multiselect>

  <Dropdown.Multiselect
    value={state.thirdValue}
    onSelectionChange={onSelectionChange3}
    defaultDisplayContent="300px menu min width"
    menuMinWidth={300}
  >
    <Dropdown.Option value="First">
      First option
    </Dropdown.Option>
    <Dropdown.Option value="Second">
      Second option!
    </Dropdown.Option>
  </Dropdown.Multiselect>
</React.Fragment>
```

Dropdown menus have a default `maxHeight` set through CSS to prevent excessively long menus when there are lots of options. This can be overridden by passing a `menuMaxHeight` prop:
```jsx
initialState = {
  value: [],
};

function onSelectionChange(value) {
  setState({ value });
}

const options = ["First", "Second", "Third", "Fourth", "oh", "my", "god", "so", "many", "options"];
const optionItems = options.map(optString => (
  <Dropdown.Option
    key={optString}
    value={optString}
  >
    {optString}
  </Dropdown.Option>
));

<Dropdown.Multiselect
  value={state.value}
  onSelectionChange={onSelectionChange}
  menuMaxHeight={100}
>
  {optionItems}
</Dropdown.Multiselect>
```

Dropdowns can have different intents if you wanted to give the button a different color:

```jsx
initialState = {
  value: [],
};

function onSelectionChange(value) {
  setState({ value });
}

const optionVals = ['First', 'Second'];
const options = optionVals.map(opt =>
  <Dropdown.Option key={opt} value={opt}>{opt}</Dropdown.Option>
);

<React.Fragment>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="default"
    buttonIntent={Dropdown.Intents.DEFAULT}
  >
    {options}
  </Dropdown.Multiselect>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="primary"
    buttonIntent={Dropdown.Intents.PRIMARY}
  >
    {options}
  </Dropdown.Multiselect>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="danger"
    buttonIntent={Dropdown.Intents.DANGER}
  >
    {options}
  </Dropdown.Multiselect>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="success"
    buttonIntent={Dropdown.Intents.SUCCESS}
  >
    {options}
  </Dropdown.Multiselect>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="warning"
    buttonIntent={Dropdown.Intents.WARNING}
  >
    {options}
  </Dropdown.Multiselect>
  <Dropdown.Multiselect
    value={state.value}
    onSelectionChange={onSelectionChange}
    defaultDisplayContent="info"
    buttonIntent={Dropdown.Intents.INFO}
  >
    {options}
  </Dropdown.Multiselect>
</React.Fragment>
```
