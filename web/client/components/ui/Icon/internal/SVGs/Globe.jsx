// @flow
import * as React from 'react';

import type { SVGProps } from 'components/ui/Icon/internal/SVGs/types';

export default function Globe(props: SVGProps) {
  return (
    <svg
      height="24"
      viewBox="5.3 4.1 14.55 14.55"
      width="24"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <path
        fill="currentColor"
        d="M12.5 4.227c-4.01 0-7.273 3.263-7.273 7.273s3.263 7.273 7.273 7.273 7.273-3.263 7.273-7.273S16.51 4.227 12.5 4.227zm.422 4.621a16.402 16.402 0 002.143-.191c.164.722.269 1.534.294 2.42h-2.437V8.848zm0-.845V5.152c.737.27 1.456 1.231 1.921 2.685-.615.093-1.26.15-1.92.166zm-.844-2.851v2.85a15.585 15.585 0 01-1.92-.165c.465-1.454 1.183-2.414 1.92-2.685zm0 3.696v2.23H9.64c.026-.887.13-1.699.294-2.421.686.108 1.405.173 2.143.191zm-3.282 2.23H6.088a6.39 6.39 0 011.085-3.171c.587.244 1.239.444 1.936.597-.178.789-.287 1.656-.313 2.573zm0 .844c.026.918.135 1.785.313 2.575-.697.152-1.349.351-1.936.596a6.386 6.386 0 01-1.085-3.17h2.708zm.845 0h2.437v2.23c-.738.017-1.457.083-2.143.19a12.63 12.63 0 01-.294-2.42zm2.437 3.075v2.85c-.737-.27-1.455-1.231-1.92-2.685.615-.092 1.259-.149 1.92-.165zm.844 2.851v-2.85c.662.016 1.306.072 1.921.165-.465 1.453-1.184 2.414-1.92 2.685zm0-3.697v-2.229h2.437c-.026.887-.13 1.698-.294 2.42a16.395 16.395 0 00-2.143-.19zm3.282-2.229h2.709a6.382 6.382 0 01-1.086 3.17 11.492 11.492 0 00-1.936-.595c.179-.79.287-1.657.313-2.575zm0-.845a13.502 13.502 0 00-.313-2.574 11.396 11.396 0 001.936-.597 6.391 6.391 0 011.086 3.171h-2.71zm1.082-3.863c-.495.19-1.035.348-1.61.472-.282-.916-.666-1.691-1.122-2.276 1.061.36 2 .987 2.732 1.804zm-6.84-1.803c-.456.584-.84 1.36-1.121 2.275a10.863 10.863 0 01-1.61-.471 6.437 6.437 0 012.73-1.804zM7.715 15.786c.495-.19 1.035-.35 1.61-.472.282.915.665 1.691 1.121 2.275a6.434 6.434 0 01-2.731-1.803zm6.84 1.803c.455-.584.84-1.36 1.121-2.275a10.84 10.84 0 011.61.472 6.454 6.454 0 01-2.731 1.803z"
      />
    </svg>
  );
}
